import azureml
from azureml.core import Run

# access the Azure ML run
# init run param to check if running within AML
def get_AMLRun():
    try:
        run = Run.get_submitted_run()
        return run
    except Exception as e:
        print("Caught = {}".format(e.message))
        return None