"""
This type stub file was generated by pyright.
"""

from git.util import IndexFileSHA1Writer
from .typ import BaseIndexEntry, IndexEntry
from typing import Dict, IO, List, Sequence, TYPE_CHECKING, Tuple, Type, Union
from git.types import PathLike
from .base import IndexFile
from git.db import GitCmdObjectDB
from git.objects.tree import TreeCacheTup

if TYPE_CHECKING: ...
S_IFGITLINK = ...
CE_NAMEMASK_INV = ...
__all__ = (
    "write_cache",
    "read_cache",
    "write_tree_from_cache",
    "entry_key",
    "stat_mode_to_index_mode",
    "S_IFGITLINK",
    "run_commit_hook",
    "hook_path",
)

def hook_path(name: str, git_dir: PathLike) -> str:
    """:return: path to the given named hook in the given git repository directory"""
    ...

def run_commit_hook(name: str, index: IndexFile, *args: str) -> None:
    """Run the commit hook of the given name. Silently ignores hooks that do not exist.

    :param name: name of hook, like 'pre-commit'
    :param index: IndexFile instance
    :param args: arguments passed to hook file
    :raises HookExecutionError:"""
    ...

def stat_mode_to_index_mode(mode: int) -> int:
    """Convert the given mode from a stat call to the corresponding index mode
    and return it"""
    ...

def write_cache(
    entries: Sequence[Union[BaseIndexEntry, IndexEntry]],
    stream: IO[bytes],
    extension_data: Union[None, bytes] = ...,
    ShaStreamCls: Type[IndexFileSHA1Writer] = ...,
) -> None:
    """Write the cache represented by entries to a stream

    :param entries: **sorted** list of entries
    :param stream: stream to wrap into the AdapterStreamCls - it is used for
        final output.

    :param ShaStreamCls: Type to use when writing to the stream. It produces a sha
        while writing to it, before the data is passed on to the wrapped stream

    :param extension_data: any kind of data to write as a trailer, it must begin
        a 4 byte identifier, followed by its size ( 4 bytes )"""
    ...

def read_header(stream: IO[bytes]) -> Tuple[int, int]:
    """Return tuple(version_long, num_entries) from the given stream"""
    ...

def entry_key(*entry: Union[BaseIndexEntry, PathLike, int]) -> Tuple[PathLike, int]:
    """:return: Key suitable to be used for the index.entries dictionary
    :param entry: One instance of type BaseIndexEntry or the path and the stage"""
    ...

def read_cache(
    stream: IO[bytes],
) -> Tuple[int, Dict[Tuple[PathLike, int], IndexEntry], bytes, bytes]:
    """Read a cache file from the given stream

    :return: tuple(version, entries_dict, extension_data, content_sha)

      * version is the integer version number
      * entries dict is a dictionary which maps IndexEntry instances to a path at a stage
      * extension_data is '' or 4 bytes of type + 4 bytes of size + size bytes
      * content_sha is a 20 byte sha on all cache file contents"""
    ...

def write_tree_from_cache(
    entries: List[IndexEntry], odb: GitCmdObjectDB, sl: slice, si: int = ...
) -> Tuple[bytes, List[TreeCacheTup]]:
    """Create a tree from the given sorted list of entries and put the respective
    trees into the given object database

    :param entries: **sorted** list of IndexEntries
    :param odb: object database to store the trees in
    :param si: start index at which we should start creating subtrees
    :param sl: slice indicating the range we should process on the entries list
    :return: tuple(binsha, list(tree_entry, ...)) a tuple of a sha and a list of
        tree entries being a tuple of hexsha, mode, name"""
    ...

def aggressive_tree_merge(
    odb: GitCmdObjectDB, tree_shas: Sequence[bytes]
) -> List[BaseIndexEntry]:
    """
    :return: list of BaseIndexEntries representing the aggressive merge of the given
        trees. All valid entries are on stage 0, whereas the conflicting ones are left
        on stage 1, 2 or 3, whereas stage 1 corresponds to the common ancestor tree,
        2 to our tree and 3 to 'their' tree.
    :param tree_shas: 1, 2 or 3 trees as identified by their binary 20 byte shas
        If 1 or two, the entries will effectively correspond to the last given tree
        If 3 are given, a 3 way merge is performed"""
    ...