import logging
import os
import pickle
import time

import numpy as np
import pandas as pd

from qmenta.sdk import __version__ as sdk_version, directory_utils

def run(context):
    """
    Example age predictor model

    Parameters
    ----------
    context : qmenta.sdk.context.AnalysisContext
    """

    analysis_data = context.fetch_analysis_data()

    logger = logging.getLogger('main')
    logger.info("Tool information: {} [v{}]".format(analysis_data['name'], analysis_data['version']))
    logger.info("SDK version: {}".format(sdk_version))

    # Hackaton folder
    hackaton_dir = os.path.expanduser('~/qmenta_cnic_1000_brains_challenge')
    
    # Input directory: we will download the files from the platform in this directory
    input_data_dir = os.path.join(hackaton_dir, 'input_data')
    directory_utils.mkdirs(input_data_dir)

    # Output directory: we will store the results of our analysis in this folder to be uploaded to the platform
    output_data_dir = os.path.join(hackaton_dir, 'output_data')
    directory_utils.mkdirs(output_data_dir)

    # Download inputs: volumetric.csv
    # Our input filter, configured in predict_age_settings.json, filters all ANTs Morphology 2.1 (v.4.6) results 
    # so that we only get the file we are interested in, volumetric.csv
    volumetric_csv_f = context.get_files(
        'input_ants',
        reg_expression="volumetric\\.csv",
        file_filter_condition_name="c_volumetric"
    )

    if len(volumetric_csv_f) == 0:
        raise RuntimeError('No \'volumetric.csv\' could be found as a result of the ANTs analysis.')

    volumetric_csv = volumetric_csv_f[0].download(input_data_dir)

    # Set progress during the analysis, that will be visible in the web platform in the form
    # of a progress bar
    context.set_progress(message='Fetched data', value=20)

    # Extract the relevant features from the volumetric.csv to run inference
    volumetric_data = pd.read_csv(volumetric_csv)
    gm_volume_value = volumetric_data.loc[volumetric_data['label'] == 'Gray matter', 'volume'].values[0]
    icv_value = volumetric_data.loc[volumetric_data['label'] == 'ICV', 'volume'].values[0]
    x = np.empty((1, 1), dtype=np.float32)
    x[0, 0] = gm_volume_value / icv_value

    context.set_progress('Loaded data from disk', value=50)

    # Load the persisted model from disk. This model has been packaged with the docker image in a known location.
    model_dir = os.path.join(hackaton_dir, 'models')
    model_pkl = os.path.join(model_dir, 'linear_regression_example.pkl')
    with open(model_pkl, 'rb') as fd:
        linear_regression_model = pickle.load(fd)

    context.set_progress('Loaded model into memory', value=70)

    # Run inference with the loaded model over the predictor data x
    prediction = linear_regression_model.predict(x)
    predicted_age = prediction[0]

    context.set_progress('Inference', value=90)

    # Write the predicted age in a text file and upload it to the platform
    result_file = os.path.join(output_data_dir, 'age.txt')
    with open(result_file, 'w') as fd:
        fd.write(predicted_age + '\n')
    context.upload_file(result_file, 'age.txt', tags={'prediction'})
