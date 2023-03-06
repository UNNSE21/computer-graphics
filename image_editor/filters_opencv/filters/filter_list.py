from typing import Final

from filters_opencv.filters.global_filters.global_filters_list import global_filters
from filters_opencv.filters.local_filters.local_filters_list import local_filters
from filters_opencv.filters.point_filters.point_filters_list import point_filters

filters: Final = point_filters + local_filters + global_filters
