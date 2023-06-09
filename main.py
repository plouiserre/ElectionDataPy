from src.Dependency.Dependency import Dependency
from src.Orchestrate.OrchestrateStoreElectionsDatas import OrchestrateStoreElectionsDatas
from src.Orchestrate.OrchestrateAdapters import OrchestrateAdapters

dependency = Dependency()
dependency.init_dependencies()
orchestrate_adapters = OrchestrateAdapters(dependency)
orchestrate_store = OrchestrateStoreElectionsDatas(dependency, orchestrate_adapters)
orchestrate_store.store_elections_datas()