__all__ = [
    "IntPointer",
    "MatLike",
    "MatShape",
    "Size",
    "Size2f",
    "Scalar",
    "Point",
    "Point2i",
    "Point2f",
    "Point2d",
    "Point3i",
    "Point3f",
    "Point3d",
    "Range",
    "Rect",
    "Rect2i",
    "Rect2d",
    "Moments",
    "RotatedRect",
    "TermCriteria",
    "Vec2i",
    "Vec2f",
    "Vec2d",
    "Vec3i",
    "Vec3f",
    "Vec3d",
    "Vec4i",
    "Vec4f",
    "Vec4d",
    "Vec6f",
    "FeatureDetector",
    "DescriptorExtractor",
    "FeatureExtractor",
    "GProtoArg",
    "GProtoInputArgs",
    "GProtoOutputArgs",
    "GRunArg",
    "GOptRunArg",
    "GMetaArg",
    "Prim",
    "Matx33f",
    "Matx33d",
    "Matx44f",
    "Matx44d",
    "GTypeInfo",
    "ExtractArgsCallback",
    "ExtractMetaCallback",
    "LayerId",
    "IndexParams",
    "SearchParams",
    "map_string_and_string",
    "map_string_and_int",
    "map_string_and_vector_size_t",
    "map_string_and_vector_float",
    "map_int_and_double",
]

import numpy
import cv2
import typing as _typing


if _typing.TYPE_CHECKING:
    NumPyArrayGeneric = numpy.ndarray[_typing.Any, numpy.dtype[numpy.generic]]
else:
    NumPyArrayGeneric = numpy.ndarray


if _typing.TYPE_CHECKING:
    NumPyArrayFloat32 = numpy.ndarray[_typing.Any, numpy.dtype[numpy.float32]]
else:
    NumPyArrayFloat32 = numpy.ndarray


if _typing.TYPE_CHECKING:
    NumPyArrayFloat64 = numpy.ndarray[_typing.Any, numpy.dtype[numpy.float64]]
else:
    NumPyArrayFloat64 = numpy.ndarray


if _typing.TYPE_CHECKING:
    TermCriteria_Type = cv2.TermCriteria_Type
else:
    TermCriteria_Type = int


IntPointer = int
"""Represents an arbitrary pointer"""
MatShape = _typing.Sequence[int]
Size = _typing.Sequence[int]
"""Required length is 2"""
Size2f = _typing.Sequence[float]
"""Required length is 2"""
Scalar = _typing.Sequence[float]
"""Required length is at most 4"""
Point = _typing.Sequence[int]
"""Required length is 2"""
Point2i = Point
Point2f = _typing.Sequence[float]
"""Required length is 2"""
Point2d = _typing.Sequence[float]
"""Required length is 2"""
Point3i = _typing.Sequence[int]
"""Required length is 3"""
Point3f = _typing.Sequence[float]
"""Required length is 3"""
Point3d = _typing.Sequence[float]
"""Required length is 3"""
Range = _typing.Sequence[int]
"""Required length is 2"""
Rect = _typing.Sequence[int]
"""Required length is 4"""
Rect2i = _typing.Sequence[int]
"""Required length is 4"""
Rect2d = _typing.Sequence[float]
"""Required length is 4"""
Moments = _typing.Dict[str, float]
RotatedRect = _typing.Tuple[Point2f, Size, float]
"""Any type providing sequence protocol is supported"""
TermCriteria = _typing.Tuple[TermCriteria_Type, int, float]
"""Any type providing sequence protocol is supported"""
Vec2i = _typing.Sequence[int]
"""Required length is 2"""
Vec2f = _typing.Sequence[float]
"""Required length is 2"""
Vec2d = _typing.Sequence[float]
"""Required length is 2"""
Vec3i = _typing.Sequence[int]
"""Required length is 3"""
Vec3f = _typing.Sequence[float]
"""Required length is 3"""
Vec3d = _typing.Sequence[float]
"""Required length is 3"""
Vec4i = _typing.Sequence[int]
"""Required length is 4"""
Vec4f = _typing.Sequence[float]
"""Required length is 4"""
Vec4d = _typing.Sequence[float]
"""Required length is 4"""
Vec6f = _typing.Sequence[float]
"""Required length is 6"""
Matx33f = NumPyArrayFloat32
"""NDArray(shape=(3, 3), dtype=numpy.float32)"""
Matx33d = NumPyArrayFloat64
"""NDArray(shape=(3, 3), dtype=numpy.float64)"""
Matx44f = NumPyArrayFloat32
"""NDArray(shape=(4, 4), dtype=numpy.float32)"""
Matx44d = NumPyArrayFloat64
"""NDArray(shape=(4, 4), dtype=numpy.float64)"""
IndexParams = _typing.Dict[str, _typing.Union[bool, int, float, str]]
SearchParams = _typing.Dict[str, _typing.Union[bool, int, float, str]]
map_string_and_string = _typing.Dict[str, str]
map_string_and_int = _typing.Dict[str, int]
map_string_and_vector_size_t = _typing.Dict[str, _typing.Sequence[int]]
map_string_and_vector_float = _typing.Dict[str, _typing.Sequence[float]]
map_int_and_double = _typing.Dict[int, float]
