from src.Dependency.Dependency import Dependency
from src.Orchestrate.OrchestrateStoreElectionsDatas import OrchestrateStoreElectionsDatas

dependency = Dependency()
dependency.init_dependencies()
orchestrate = OrchestrateStoreElectionsDatas(dependency)
orchestrate.store_elections_datas()