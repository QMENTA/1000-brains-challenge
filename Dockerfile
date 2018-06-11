FROM ubuntu:16.04

# Install basic software
RUN apt-get update && apt-get install -y curl python bzip2 && rm -rf /var/lib/apt/lists/*

# Install miniconda
RUN curl https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh > ${HOME}/miniconda_installer.sh && \
    /bin/bash ${HOME}/miniconda_installer.sh -b -p /opt/miniconda && \
    ln -s /opt/miniconda/bin/conda /usr/local/bin/conda && \
    ln -s /opt/miniconda/bin/activate /usr/local/bin/activate && \
    ln -s /opt/miniconda/bin/deactivate /usr/local/bin/deactivate && \
    rm ${HOME}/miniconda_installer.sh

# Install conda environment
COPY environment.yml /root/environment.yml
RUN conda env create -f /root/environment.yml
RUN rm /root/environment.yml

# Package the SDK script
RUN mkdir -p /root/src
COPY predict_age.py /root/src/predict_age.py
ENV PYTHONPATH="/root/src/:${PYTHONPATH}"

# Package the persisted model
RUN mkdir -p /root/qmenta_cnic_1000_brains_challenge/models
COPY linear_regression_example.pkl /root/qmenta_cnic_1000_brains_challenge/models/linear_regression_example.pkl

# Create entrypoint
RUN printf "#!/bin/bash\n" >> /root/entrypoint.sh
RUN printf "\n# Start command\nexec /opt/miniconda/envs/qmenta_1000_brains/bin/python -m qmenta.sdk.executor \$@\n" >> /root/entrypoint.sh
RUN chmod u+x /root/entrypoint.sh

WORKDIR "/root"