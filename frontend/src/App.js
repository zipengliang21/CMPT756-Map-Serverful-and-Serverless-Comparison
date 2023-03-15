import Graph from "react-graph-vis";
import React, { useState } from "react";
import styled from "styled-components";
import Github from "./components/Github";
import Bug from "./components/Bug";

const options = {
    layout: {
        hierarchical: false
    },
    edges: {
        color: "#000000"
    }
};

function randomColor() {
    const red = Math.floor(Math.random() * 256).toString(16).padStart(2, '0');
    const green = Math.floor(Math.random() * 256).toString(16).padStart(2, '0');
    const blue = Math.floor(Math.random() * 256).toString(16).padStart(2, '0');
    return `#${red}${green}${blue}`;
}

const AppWrapper = styled.div`
  background: #FBFAF6;
  display: flex;
  min-height: 100vh;
  flex-direction: column;
`;

const HeaderWrapper = styled.header`
  background-color: #FBFAF6;
  border-bottom: #f2f2f2;
  height: 80px;
  @media(max-width: 1280px) {
    height: 255px;
  };
  .box{
      width: 70%;
      height: 100%;
      margin: 10px auto;
      padding: 0 12px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      @media(max-width: 576px) {
        flex-direction: column;
        justify-content: center;
      };
      .boxLeft{
          font-family: Poppins, sans-serif;
          line-height: 1.8;
          text-transform: uppercase;
          color: rgb(3, 37, 108);
          font-size: 1.4em;
          @media(max-width: 576px) {
            margin: 10px 0 10px 0;
          };
      }
      .boxLeft::after {
        @media(max-width: 992px) {
            content: "";
            margin-left: 0;
        };
        content: "◦◦◦";
        margin-left: 0.5em;
        color: #80B2ED;
      }
      .boxRight{
        display: inline-flex;
        justify-content: flex-start;
        @media(max-width: 576px) {
            margin-right: 0;
            margin-bottom: 15px;
            flex-direction: column;
            justify-content: center;
        };
        p{
          margin: 0px 35px;
          font-size: 1.4em;
          font-family: Poppins, sans-serif;
          line-height: 1.8;
          font-weight: 450;
          color: rgb(3, 37, 108);
          @media(max-width: 992px) {
              margin: 200px 20px;
              text-align: center;
          };
          @media(max-width: 576px) {
              margin: 200px 2px;
              text-align: center;
          };
        }
      }
 }
`;

const Footer = styled.div`
  padding: 1em 0;
  justify-content: center;
  align-items: center;
  text-align: center;
`;

function App() {
    const [state, setState] = useState({
        counter: 5,
        graph: {
            nodes: [
                { id: 1, label: "Node 1", color: "#e04141" },
                { id: 2, label: "Node 2", color: "#e09c41" },
                { id: 3, label: "Node 3", color: "#e0df41" },
                { id: 4, label: "Node 4", color: "#7be041" },
                { id: 5, label: "Node 5", color: "#41e0c9" }
            ],
            edges: [
                { from: 1, to: 2 },
                { from: 1, to: 3 },
                { from: 2, to: 4 },
                { from: 2, to: 5 }
            ]
        },
        events: {
            select: ({ nodes, edges }) => {
                console.log("Selected nodes:");
                console.log(nodes);
                console.log("Selected edges:");
                console.log(edges);
                alert("Selected node: " + nodes);
            },
            doubleClick: ({ pointer: { canvas } }) => {
            }
        }
    })
    const { graph, events } = state;
  return (
      <AppWrapper>
          <HeaderWrapper>
              <div className="box">
                  <div to="/">
                      <div className="boxLeft"><span style={{fontWeight: 800}}>CMPT756</span></div>
                  </div>
                  <div className="boxRight">
                      <p>Map App - Comparing Serverless and Serverful Performance Using Microservices Architecture</p>
                  </div>
                  <div></div>
              </div>
          </HeaderWrapper>
          <Graph graph={graph} options={options} events={events} style={{ height: "85vh" }} />
          <Footer>
              <div>
                  <Github/> Group 5 Demo <Bug/>
              </div>
              <div>Copyright © Made by Chifeng Wen, Zipeng Liang, Shung Ho Jonathan Au, Hossain Mahbub, and Min Fei,
              </div>
          </Footer>
      </AppWrapper>
  );
}

export default App;
