import axios from 'axios';
import React, {useState} from "react";
import styled from "styled-components";
import Github from "./components/Github";
import Bug from "./components/Bug";
import {useNode} from "./hooks/useNode";

const AppWrapper = styled.div`
  background: #FBFAF6;
  display: flex;
  min-height: 100vh;
  flex-direction: column;
`;

const InputWrapper = styled.div`
  border: 3px solid #89CFF0;
  width: 500px;
  margin: 0 auto;
  text-align: center;
  div{
    padding: 10px;
    input{
      margin-left: 10px;
    }
  }
`;
const TableWrapper = styled.div`
  display: flex;
  width: 500px;
  margin: 30px auto 0 auto;
  text-align: center;
  table{
    padding-right: 100px;
  }
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
          margin: 0 35px;
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
    const {nodes, links} = useNode();

    const [sourceId, setSourceId] = useState(null);
    const [destinationId, setDestinationId] = useState(null);
    const [path, setPath] = useState("")

    function handleSourceIdChange(event) {
        setSourceId(event.target.value);
    }

    function handleDestinationIdChange(event) {
        setDestinationId(event.target.value);
    }

    function handleConfirmClick() {
        const data = {
            start_node_id: parseInt(sourceId),
            dst_node_id: parseInt(destinationId),
        };
        axios.post(`http://navigation.e8yes.org/queryPath`, data)
            .then(response => {
                console.log(response)
                const path = response.data.join(" -> ");
                setPath(path);
            })
            .catch(error => console.log(error));
    }

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
          <InputWrapper>
              <div>
                  <label htmlFor="source-id">Source Node ID:</label>
                  <input id="source-id" type="text" value={sourceId} onChange={handleSourceIdChange} />
              </div>
              <div>
                  <label htmlFor="destination-id">Destination Node ID:</label>
                  <input id="destination-id" type="text" value={destinationId} onChange={handleDestinationIdChange} />
              </div>
              <button onClick={handleConfirmClick}>Confirm</button>
              <div style={{color: "red"}}>Result: {path}</div>
          </InputWrapper>
          <TableWrapper>
              <table>
                  <thead>
                  <tr>
                      <th>id</th>
                      <th>x</th>
                      <th>y</th>
                      <th>importance</th>
                  </tr>
                  </thead>
                  <tbody>
                  {nodes.map(node => (
                      <tr key={node.id}>
                          <td>{node.id}</td>
                          <td>{node.x.toFixed(3)}</td>
                          <td>{node.y.toFixed(3)}</td>
                          <td>{node.importance.toFixed(2)}</td>
                      </tr>
                  ))}
                  </tbody>
              </table>
              <table>
                  <thead>
                  <tr>
                      <th>loc1_id</th>
                      <th>loc2_id</th>
                      <th>distance</th>
                  </tr>
                  </thead>
                  <tbody>
                  {links.map(link => (
                      <tr key={`${link.loc1_id} + "_" + ${link.loc2_id}`}>
                          <td>{link.loc1_id}</td>
                          <td>{link.loc2_id}</td>
                          <td>{link.distance.toFixed(3)}</td>
                      </tr>
                  ))}
                  </tbody>
              </table>
          </TableWrapper>


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
