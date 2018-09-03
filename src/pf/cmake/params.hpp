#ifndef PF_CMAKE_CONFIGURE_PARAMS_HPP_INCLUDED
#define PF_CMAKE_CONFIGURE_PARAMS_HPP_INCLUDED

#include <string>

#include <pf/fs.hpp>

namespace pf {
namespace cmake {

struct configure_params {
    std::string name;
    std::string root_namespace;
    std::string first_file_stem;
    fs::path    directory;
    bool        separate_headers   = false;
    bool        create_third_party = true;
    bool        create_examples    = true;
    bool        create_extras      = false;
    bool        create_tests       = true;
};

}  // namespace cmake
}  // namespace pf

#endif  // PF_CMAKE_CONFIGURE_PARAMS_HPP_INCLUDED
