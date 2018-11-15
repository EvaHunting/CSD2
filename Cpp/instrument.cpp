#include <iostream>

class Instrument  {
public:             // public acces specifier
  // declare constructors
  Instrument();
  Instrument(std::string sound);

  // methods (class function)
  void makesound() {
  std::cout << "sound" << std::endl;
  }
};
