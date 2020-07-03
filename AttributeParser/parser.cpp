// https://www.hackerrank.com/challenges/attribute-parser/problem

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <map>
#include <string>
#include <bits/stdc++.h>

struct element {
    std::string name;
    std::map<std::string, std::string> attributes;
    std::vector<element> elements;
};

// <tag1 value = "HelloWorld">
element parseTag(std::string tag) {
    // Remove '<', and '>' characters
    tag = tag.substr(1, tag.length()-2); // substr(start, len)
    std::stringstream ss(tag);

    // Read name
    std::string name, attribute, value;
    char ch;
    ss >> name;

    element el = element();
    el.name = name;

    // Read attributes           
    while(ss >> attribute) {
        // read in the ' = ' (space, equal, space) and the value
        ss >> ch >> value;
        // strip value of the encasing double quotes (")
        value = value.substr(1, value.length()-2); // substr(start, len)
        // add attribute to element
        el.attributes.insert(std::pair<std::string, std::string>(attribute, value));
    }

    return el;
}

void parseElements(std::vector<element> &parsed, int numTags) {
    std::stack<element*> stack;
    for(int i=0; i < numTags; i++) {
        // Read in tag line from stdin
        std::string tag;
        std::getline(std::cin, tag);
        
        if(tag[1] == '/') {
            // if closing tag '/' pop top of stack
            stack.pop();
        } else {
            // if opening tag, parse tag
            element newElement = parseTag(tag);            
            
            if(stack.size() > 0) {
                // if stack items exist then add newElement as sub element
                element *topEl = stack.top();
                topEl->elements.push_back(newElement);
                // Add element just pushed to the top of stack
                stack.push(&topEl->elements.back());
            } else {
                // if stack is empty, add element to parsed list
                parsed.push_back(newElement);
                // Add element just pushed to top of stack
                stack.push(&parsed.back());
            }
        }
    }
}

void parseQuery(std::vector<element> elements) {
    // Read in query
    std::string query;
    std::getline(std::cin, query);

    // Find tilde ~ and split query between tag and attribute
    int tildeIndex = query.find("~");
    std::string tags = query.substr(0, tildeIndex);
    std::string attribute = query.substr(tildeIndex+1, query.length()-tildeIndex);
    
    // loop through tag portion of query
    int dotIndex;
    element *currentElement = NULL;
    std::vector<element> currentElements = elements;
    while(true) {        
        dotIndex = tags.find(".");
        std::string tag;
        if(dotIndex <= 0) {
            tag = tags;
        } else {
            // Split tag string at the dotIndex
            tag = tags.substr(0, dotIndex);
            tags = tags.substr(dotIndex+1, tags.length()-dotIndex);
        }

        bool tagFound = false;
        for(element e: currentElements) {
            if (e.name == tag) {
                currentElement = &e;
                currentElements = currentElement->elements;
                tagFound = true;
                break;
            }
        }
        if (!tagFound) {
            std::cout << "Not Found!" << std::endl;
            return;
        }

        if (dotIndex <=0) {
            break;
        }
    } // end of while loop

    // If we made it to this point, a valid element was found for the query
    // Now pull the attribute if it exists.
    try {
        std::string value = currentElement->attributes.at(attribute);
        std::cout << value << std::endl;
    } catch (...) {
        std::cout << "Not Found!" << std::endl;
    }
}

/************************
 * To compile:
 * $ g++ parser.cpp -g
 * **********************/
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */        

    // Get N & Q
    int n, q;
    std::cin >> n >> q;
    std::cin.ignore(); // ignore the newline character first line: n q

    // Parse elements    
    std::vector<element> myElements;
    parseElements(myElements, n);

    // Parse queries
    for(int i=0; i < q; ++i) {
        parseQuery(myElements);
    }
    return 0;
}