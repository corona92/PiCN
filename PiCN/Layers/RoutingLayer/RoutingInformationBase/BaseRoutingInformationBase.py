
from typing import Iterator, List, Tuple

import abc
from datetime import datetime

from PiCN.Layers.ICNLayer.ForwardingInformationBase import BaseForwardingInformationBase, ForwardingInformationBaseEntry
from PiCN.Packets import Name


class BaseRoutingInformationBase(abc.ABC):
    """
    Abstract base class to be implemented by RoutingInformationBase classes.
    """

    @abc.abstractmethod
    def __init__(self, shortest_only: bool = True):
        """
        Initialize a Routing Information Base
        :param shortest_only: Whether to only add the shortest route to the FIB, or to add all routes.
        """
        pass

    @abc.abstractmethod
    def ageing(self):
        """
        Remove outdated entries from the RIB.
        """
        pass

    @abc.abstractmethod
    def insert(self, name: Name, fid: int, distance: int, timeout: datetime = None):
        """
        Insert a new route into the RIB.
        :param name: The ICN name of the route
        :param fid: The face ID  of the route
        :param distance: The distance of the route
        :param timeout: The timestamp after which to consider the route
        :return:
        """
        pass

    @abc.abstractmethod
    def build_fib(self) -> List[ForwardingInformationBaseEntry]:
        """
        Construct FIB entries from the RIB data.
        """
        pass

    @abc.abstractmethod
    def __iter__(self) -> Iterator[Tuple[Name, int, int, datetime]]:
        """
        Creates an iterator over the longest-common-prefix-reduced entries of the RIB.
        :return: An iterator of tuples (name, fid, distance, timeout)
        """
        pass

    @abc.abstractmethod
    def entries(self) -> List[Tuple[Name, int, int, datetime]]:
        """
        Creates a list of longest-common-prefix-reduced entries of the RIB.
        :return: A list of tuples (name, fid, distance, timeout)
        """
        pass

    @abc.abstractmethod
    def __len__(self):
        """
        Length of the longest-common-prefix-reduced entries of the RIB.
        :return: Length of the entries that would be added to the FIB.
        """
        pass
