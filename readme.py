#install tous les packages AZURE
pip install azure
pip uninstall -y $(pip list |grep azure | awk '{print $1}')
pip list | grep azure

# Check installation of the Azure SDK for Python
pip show azure
# Check installation of a specific library
pip show azure-storage-blob


pip install azure-storage-blob
pip install azure-monitor