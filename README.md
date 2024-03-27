# Time Drift Detection in Business Process Event Streams

## Description of Objective
Changes - be it internal or external - affect the organization's workflows and therefore the data recorded. This work focuses on detecting concept drifts in the execution time of a business process - the time perspective - in a streaming environment. Fig. shows a graphic visualization of the problem using a simplified production process. Activities in the process are represented as blue boxes. Each product has to be manufactured, delivered and accounted for. However, accounting can be done parallel to manufacturing and delivering, as shown in the concurrent branches. The length of the boxes indicates the execution time needed for this particular activity. From the left process to the right there is a tremendous change in the execution time of the accounting activity indicating a concept drift in the time perspective in this particular process.

![Visually Represented Concept Drift in the Time Perspective](Images/timedriftpicture.png)

(Note: This picture is taken from the publication:Richter, F., & Seidl, T. (2017). TESSERACT: time-drifts in event streams using series of evolving rolling averages of completion times. In Business Process Management: 15th International Conference, BPM 2017, Barcelona, Spain, September 10–15, 2017, Proceedings 15 (pp. 289-305). Springer International Publishing. )

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Docker installed on your machine. You can download Docker Desktop for Windows and Mac from [Docker Hub](https://hub.docker.com/?overlay=onboarding).

## Installation

To install the project, follow these steps:

1. Clone the repository to your local machine:
     git clone https://github.com/joris68/Concept-Drift-Detection-Event-Stream.git

2.  Navigate into the project directory:
     cd yourprojectname

## Usage

Here's how to run the project in a Docker container:

1. Build the Docker image:
     docker build -t yourprojectname .

2. Once the image is built, run the Docker container:
     docker run -p 4000:80 yourprojectname


## Contributing to the Project

1. Create a pull request


## License

This project is under Apache License 2.0