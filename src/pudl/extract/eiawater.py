"""Retrieve data from EIA Thermoelectric Cooling Water Data spreadsheets for analysis.

This modules pulls data from EIA's published Excel spreadsheets.

This code is for use analyzing EIA Thermoelectric Cooling Water Data.
"""
import logging

from pudl.extract import excel
from pudl.settings import EiaWaterSettings

logger = logging.getLogger(__name__)

# Some oddities I've discovered in the water data:
# See boiler_id CC4, it corresponds to many generators, but they're not explicitly separated.
# In the boiler_generator_assn_eia860 table we can see it is associated with generator C4-1 and C4-2 at the same time.
# In some cases there are many to many relations from generator to boiler in the water data.
# Not sure what to do about the differing levels of aggregation within the table. Potentially filtering the data into
# separate tables based on the boiler_id and generator_id columns based on the permutations of relationships


class Extractor(excel.GenericExtractor):
    """Extractor for the excel dataset EIA Thermoelectric Cooling Water Data."""

    def __init__(self, *args, **kwargs):
        """Initialize the module.

        Args:
            ds (:class:datastore.Datastore): Initialized datastore.
        """
        self.METADATA = excel.Metadata("eiawater")
        self.cols_added = []
        super().__init__(*args, **kwargs)

    def extract(self, settings: EiaWaterSettings = EiaWaterSettings()):
        """Extracts dataframes.

        Returns dict where keys are page names and values are
        DataFrames containing data across given years.

        Args:
            settings: Object containing validated settings
                relevant to EIA 860. Contains the tables and years to be loaded
                into PUDL.
        """
        return super().extract(year=settings.years)
