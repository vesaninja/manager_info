import React, { useState, useEffect } from 'react'
import './App.css';
import logo from './images/logo.png'
import demo from './images/demo.jpg'
import raitsukkaliini from './images/raitsukkaliini.jpg'
import nysse from './images/nysse.jpg'
import { Card, Image, Row, Col, ListGroup, CardGroup} from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  const [nowPlaying, setNowPlaying] = useState({name: 'Vauhti kiihtyy', albumArt: demo})
  const [currentTime, setCurrentTime] = useState(new Date());
  
  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentTime(new Date());
      }, 60 * 1000);
    return () => {
      clearInterval(timer);
    }
  }, []);

  const date = currentTime.toLocaleDateString('fi');
  const time = currentTime.toLocaleTimeString('fi');


  return (
    <div className="App">
        <div className="App-header">
          Glorious Infonäyttö
        </div>
        <Row style={{height: '40%'}}>
          <CardGroup style={{ width: '45%' }}>
            {/*Bussi aikataulukortti*/}
            <Card >
              <Card.Img variant="top" src={nysse} style={{height: '20%'}}/>
              <Card.Body>
                <Card.Title>Rengas juna aika taulu</Card.Title>
                <Card.Subtitle className="mb-2 text-muted">pysäkilta Hervannan kampus</Card.Subtitle>
                  <ListGroup variant="flush">
                    <ListGroup.Item>5 @ 14:14</ListGroup.Item>
                    <ListGroup.Item>36 @ 14:14</ListGroup.Item>
                    <ListGroup.Item>38 @ 14:17</ListGroup.Item>
                    <ListGroup.Item>58x @ 14:22</ListGroup.Item>
                    <ListGroup.Item>5 @ 14:29</ListGroup.Item>
                  </ListGroup>
              </Card.Body>
            </Card>
            {/*Ratikka aikataulukortti*/}
            <Card >
              <Card.Img variant="top" src={raitsukkaliini} style={{height: '20%'}}/>
              <Card.Body>
                <Card.Title>Hiljainen juna aika taulu</Card.Title>
                <Card.Subtitle className="mb-2 text-muted">pysäkilta Hervantakeskus A</Card.Subtitle>
                  <ListGroup variant="flush">
                    <ListGroup.Item>3 @ 14:12</ListGroup.Item>
                    <ListGroup.Item>3 @ 14:19</ListGroup.Item>
                    <ListGroup.Item>3 @ 14:27</ListGroup.Item>
                    <ListGroup.Item>3 @ 14:34</ListGroup.Item>
                    <ListGroup.Item>3 @ 14:42</ListGroup.Item>
                  </ListGroup>
              </Card.Body>
            </Card>
          </CardGroup>
          
          {/*spacer*/}
          <Col style={{ width: '33%'}}/>
          {/*Newton ruokalista*/}
          <Card style={{ width: '15%' }}>
            <Card.Body>
              <Card.Title>Newton</Card.Title>
              <Card.Text>
                -mureke
              </Card.Text>
            </Card.Body>
          </Card>
          {/*Hertsi ruokalista*/}
          <Card style={{ width: '15%' }}>
            <Card.Body>
              <Card.Title>Hertsi</Card.Title>
              <Card.Text>
                -mureke
              </Card.Text>
            </Card.Body>
          </Card>
          {/*Reaktori ruokalista*/}
          <Card style={{ width: '15%' }}>
          <Card.Body>
            <Card.Title>Reaktori</Card.Title>
            <Card.Text>
              -mureke
            </Card.Text>
          </Card.Body>
        </Card>
        </Row>
        {/*spacer*/}
        <Row style={{height: '30%'}}>
        </Row>
        <Row style={{height: '20%'}}>
          {/*logo*/}
          <Col style={{ width: '33%'}}>
            <Image src={logo} rounded style={{ height: 150 }}/>
          </Col>
          {/*spotify now playing*/}
          <Col style={{ width: '33%'}}>
            Now Playing: { nowPlaying.name }
              <br></br>
            <Image src={nowPlaying.albumArt} style={{ height: 150 }}/>
          </Col>
          {/*aika*/}
          <Col style={{ width: '33%', bottom: "0px"}}>
            <h1>{date}</h1>
            <h2>{time}</h2>            
          </Col>
        </Row>
    </div>
  );
}

export default App;
