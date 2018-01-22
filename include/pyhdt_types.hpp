/**
 * hdt_types.hpp
 * Author: Thomas MINIER - MIT License 2017-2018
 */

#ifndef PYHDT_TYPES_HPP
#define PYHDT_TYPES_HPP

#include <string>
#include <tuple>
#include <list>

// A RDF Triple. RDF terms are represented as simple strings by HDT.
typedef std::tuple<std::string, std::string, std::string> triple;

// A list of RDF triples
typedef std::list<triple> triple_list;

#endif /* PYHDT_TYPES_HPP */