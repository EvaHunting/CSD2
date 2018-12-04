#include <iostream>
#include "instrument.h"

Instrument::Instrument(std::string snd) {
  this->sound = snd;
}

Instrument::Instrument(std::string snd, int ptch) {
  this->sound = snd;
  this->pitch = ptch;
  std::cout << "pitch: " << ptch << std::endl;
}

Instrument::Instrument(std::string snd, int ptch, int volm) {
  this->sound = snd;
  this->pitch = ptch;
  std::cout << "pitch: " << ptch << std::endl;
  this->volume = volm;
  std::cout << "volume: " << volm << std::endl;
}
