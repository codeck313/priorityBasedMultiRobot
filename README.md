
<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<div align="center">


<h3 align="center">Multi Robot Path Planning Using Priority Based Algorithm</h3>

  <p align="center">
    Path Planning for Multiple Robots using D*
    <br />
    <br />
    <a href="https://youtu.be/BczI1wkpxww">View Presentation</a>
    ·
    <a href="https://github.com/codeck313/priorityBasedMultiRobot/issues">Report Bug</a>

  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage-and-results">Usage and Results</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Code for the paper [Multi Robot Path Planning Using Priority Based Algorithm](https://ieeexplore.ieee.org/document/9865690).

In this paper we describe an algorithm for planning for multiple robots with multiple goal points. We use the D* Algorithm as a backbone to create a priority based planner, further we define four scenes to evaluate the performance of the algorithm and compare the time taken for each scene. We also propose an architecture for directing multiple robots in a centralized manner using Robot Operating System (ROS). The evaluation of both the algorithm and control architecture is done using a simulation in the Gazebo environment.

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- GETTING STARTED -->


## Installation

1. Clone the repo
   ```sh
   git clone https://github.com/codeck313/priorityBasedMultiRobot.git
   ```
2. Install Requirements
   ```sh
   pip3 install -r requirements.txt
   ```
4. Update the input.yaml with the required parameters four example inputs are provided

5. Run the planning script
   ```sh
    python3 hillClimber.py sample_maps/input.yaml
   ```

5. Run the visualization script
   ```sh
    python3 visualize.py sample_maps/input.yaml output.yaml
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage and Results

1. [Narrow Corridor Map](https://youtu.be/kaAiMFwgDOE)
![Narrow Corridor Map](https://github.com/codeck313/priorityBasedMultiRobot/gifs/narrow.gif)

2. [City Block Map](https://youtu.be/HLbFQVABfxw)
![City Blocks Map](https://github.com/codeck313/priorityBasedMultiRobot/gifs/city_case.gif)

3.  Cross Road Map
![Cross Road](https://github.com/codeck313/priorityBasedMultiRobot/gifs/plus_case.gif)

4. General Case Map
![General Case](https://github.com/codeck313/priorityBasedMultiRobot/gifs/general_case-1.gif)

5. [Square Park Map](https://youtu.be/mJgmVen-9D4)

_For more information, please refer to our [paper](https://ieeexplore.ieee.org/document/9865690)
and [presentation video](https://youtu.be/BczI1wkpxww)_
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Path Planning for Multiple Robots
- [ ] C++ Implementation
- [ ] Converting Discrete Paths to Trajectories
- [ ] Optimization
- [ ] SLAM Integration

See the [open issues](https://github.com/codeck313/priorityBasedMultiRobot/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Naman - [@NamanMenezes17](https://twitter.com/NamanMenezes17)

Saksham  [@The Lowest Type](https://thelowesttype.github.io/)

Project Link: [https://github.com/codeck313/priorityBasedMultiRobot](https://github.com/codeck313/priorityBasedMultiRobot)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* Code for visualization was taken from [multi_agent_path_planning](https://github.com/atb033/multi_agent_path_planning)
* [AIRL Laboratory IISc](https://github.com/IISc-AIRL)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/codeck313/priorityBasedMultiRobot.svg?style=for-the-badge
[contributors-url]: https://github.com/codeck313/priorityBasedMultiRobot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/codeck313/priorityBasedMultiRobot.svg?style=for-the-badge
[forks-url]: https://github.com/codeck313/priorityBasedMultiRobot/network/members
[stars-shield]: https://img.shields.io/github/stars/codeck313/priorityBasedMultiRobot.svg?style=for-the-badge
[stars-url]: https://github.com/codeck313/priorityBasedMultiRobot/stargazers
[issues-shield]: https://img.shields.io/github/issues/codeck313/priorityBasedMultiRobot.svg?style=for-the-badge
[issues-url]: https://github.com/codeck313/priorityBasedMultiRobot/issues
[license-shield]: https://img.shields.io/github/license/codeck313/priorityBasedMultiRobot?label=license&style=for-the-badge
[license-url]: https://github.com/codeck313/priorityBasedMultiRobot/blob/main/LICENSE.txt
