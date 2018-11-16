#include <iostream>

class Instrument  {
public:             // public acces specifier
  // declare constructors
  Instrument();
  Instrument(std::string snd);
  Instrument(std::string snd, int ptch);
  Instrument(std::string snd, int ptch, int volm);

  //  variables
  std::string sound;
  int pitch;
  int volume;

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
