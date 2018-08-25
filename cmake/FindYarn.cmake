set(_prev "${YARN_EXECUTABLE}")
find_program(YARN_EXECUTABLE yarn DOC "Path to Yarn, the better NPM")

if(YARN_EXECUTABLE)
    if(NOT _prev)
        message(STATUS "Found Yarn executable: ${YARN_EXECUTABLE}")
    endif()
    set(Yarn_FOUND TRUE CACHE INTERNAL "")
else()
    set(Yarn_FOUND FALSE CACHE INTERNAL "")
    if(Yarn_FIND_REQUIRED)
        message(FATAL_ERROR "Failed to find a Yarn executable")
    endif()
endif()
