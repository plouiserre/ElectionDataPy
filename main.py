from src.Dependency.Dependency import Dependency
from src.Workflow.WorkflowManager import WorkflowManager

dependency = Dependency()
dependency.init_dependencies()
workflow = WorkflowManager(dependency)
workflow.store_datas()