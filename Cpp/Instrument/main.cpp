#include <iostream>
#include "instrument.h"

int main()  {
  int hulp;
  Instrument instrument1("Tuut");
  instrument1.play();
  std::cout << "Pitch: ";
  std::cin >> hulp;
  instrument1.pitch = hulp;
  std::cout << "Volume: ";
  std::cin >> hulp;
  instrument1.volume = hulp;

  Instrument instrument2("Biem");
  instrument2.play();
  std::cout << "Pitch: ";
  std::cin >> hulp;
  instrument2.pitch = hulp;
  std::cout << "Volume: ";
  std::cin >> hulp;
  instrument2.volume = hulp;
return(0);
}
