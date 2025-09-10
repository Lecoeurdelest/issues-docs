FROM continuumio/miniconda3:23.5.2-0

WORKDIR /app

# Create Conda environment with Python 3.11
RUN conda create -n uc_env python=3.11.13 && \
    echo "source activate uc_env" > ~/.bashrc
ENV PATH /opt/conda/envs/uc_env/bin:$PATH

# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

EXPOSE 8008

CMD ["bash"]
