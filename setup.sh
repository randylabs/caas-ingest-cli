echo "Starting installation"
python3 -m venv .venv
echo "Virtual environment created"

echo "Activating the virtual environment"
source .venv/bin/activate
echo "Installing dependencies..."
pip install -r requirements.txt
echo "Finished installation"
echo ""
echo "If you want to use the ingestion script you have to activate the virtual environment before doing so."
echo "You can activate it by running the following command:"
echo "source .venv/bin/activate"
echo ""
echo "Then use the following command to view the helper of the service which will show more commands."
echo "python3 ingest.py"
echo ""
echo "Once you are done with using the ingestion script you can use the following command to deactivate the virtual environment:"
echo "deactivate"
