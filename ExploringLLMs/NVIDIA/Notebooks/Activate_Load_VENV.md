# Create Virtual Environment
1. Open Anaconda.
2. Environments: Create Virtual Environment,
   Environment will be created at location:
   >> /opt/anaconda3/envs
3. Activate the VENV:
   >> conda activate venv


# Load the virtual environment to ipykernel
    Note: Virtual environment should be activated.
1. pip install --user ipykernel
2. python -m ipykernel install --user --name=venv
   Kernel location:
   >>> /Users/shubhamrathod/Library/Jupyter/kernels

# Other useful command
1. conda deactivate venv
2. conda env remove -n venv
3. jupyter kernelspec list
4. jupyter kernelspec uninstall venv