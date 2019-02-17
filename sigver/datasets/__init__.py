from .gpds import GPDSDataset
from .mcyt import MCYTDataset
from .cedar import CedarDataset
from .brazilian import BrazilianDataset, BrazilianDatasetWithoutSimpleForgeries
from .utsig import UTSIGDataset

available_datasets = {'gpds': GPDSDataset,
                      'mcyt': MCYTDataset,
                      'cedar': CedarDataset,
                      'brazilian': BrazilianDataset,
                      'brazilian-nosimple': BrazilianDatasetWithoutSimpleForgeries,
                      'utsig': UTSIGDataset}
