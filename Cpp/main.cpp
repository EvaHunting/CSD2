#include <iostream>

class Instrument  {
public:             // public acces specifier
  // declare constructors
  Instrument();
  Instrument(std::string snd);

  std::string sound;

  // methods (class function)
  void makesound() {
  std::cout << sound << std::endl;
  }

  void play()  {
    makesound();
  }
};

Instrument::Instrument(std::string snd) {
  this->sound = snd;
}



int main()  {
  Instrument instrument1("Tuut");
  Instrument instrument2("Biem");
  instrument1.play();
  instrument2.play();
return(0);
}
