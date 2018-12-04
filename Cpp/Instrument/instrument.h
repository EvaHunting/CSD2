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
