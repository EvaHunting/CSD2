#include <iostream>

class Instrument  {
public:             // public acces specifier
  // declare constructors
  Instrument();
  Instrument(std::string snd);
  Instrument(std::string snd, int ptch);
  Instrument(std::string snd, int ptch, int volm);

  std::string sound;

  // methods (class function)
  void makesound() {
  std::cout << sound << std::endl;
  }

  int pitch;
  int volume;

  void play()  {
    makesound();
  }
};

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

int main(int argc, char* argv[])  {
  Instrument instrument1("Tuut", 440, 100);
  instrument1.play();
  Instrument instrument2("Biem", 500, 127);
  instrument2.play();
return(0);
}
