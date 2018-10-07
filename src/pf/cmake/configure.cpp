#include "./configure.hpp"

// Maybe better design: split up the actual configure execution and processing.
// E.g. take in a function_ref, which is invoked with the processed args
void pf::cmake::configure(pf::cmake::configure_params const&) {
    // bp::system(bp::search_path("cmake"), bp::std_out > stdout);  //
}
