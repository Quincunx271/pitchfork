#ifndef PF_CMAKE_CONFIGURE_PARAMS_HPP_INCLUDED
#define PF_CMAKE_CONFIGURE_PARAMS_HPP_INCLUDED

#include <string>
#include <vector>

#include <pf/fs.hpp>

namespace pf {
namespace cmake {

enum class standard_version {
    v98,
    v03,
    v11,
    v14,
    v17,
    v20,
};

enum class build_type {
    empty,
    debug,
    release,
    relwithdebinfo,
    minsizerel,
};

// Ideally, these params should match closely the VSCode CMake Tools extension
struct configure_params {
    fs::path cmake_exe;

    std::string project_name;

    fs::path source_directory;
    fs::path build_directory;

    std::string      generator;
    standard_version version;
    build_type       _build_type;

    std::vector<std::string> extra_args;
};

}  // namespace cmake
}  // namespace pf

#endif  // PF_CMAKE_CONFIGURE_PARAMS_HPP_INCLUDED
