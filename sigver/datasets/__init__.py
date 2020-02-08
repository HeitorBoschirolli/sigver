from .gpds import GPDSDataset
from .mcyt import MCYTDataset
from .cedar import CedarDataset
from .brazilian import BrazilianDataset, BrazilianDatasetWithoutSimpleForgeries
from .utsig import UTSIGDataset
from .bg_utsig import BGUTSIGDataset
from .augmented_utsig import AugmentedUTSIGDataset
from .utsig_mini import MiniUTSIGDataset
from .utsig_augmented_mini import AugmentedMiniUTSIGDataset

available_datasets = {'gpds': GPDSDataset,
                      'mcyt': MCYTDataset,
                      'cedar': CedarDataset,
                      'brazilian': BrazilianDataset,
                      'brazilian-nosimple': BrazilianDatasetWithoutSimpleForgeries,
                      'utsig': UTSIGDataset,
                      'bg_utsig': BGUTSIGDataset,
                      'augmented_utsig': AugmentedUTSIGDataset,
                      'utsig_mini': MiniUTSIGDataset,
                      'utsig_augmented_mini': AugmentedMiniUTSIGDataset}
