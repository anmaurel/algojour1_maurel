import axios from "axios";
import React from "react";
import { BlocChain } from "./entities";

interface IOwnState {
  blocChain: BlocChain;
}

class Home extends React.PureComponent<{}, IOwnState> {
  state = {
    blocChain: [] as BlocChain,
  };
  componentDidMount() {
    axios
      .get(`http://127.0.0.1:4000/`)
      .then((res) => {
        const blocChain = res.data;
        this.setState({ blocChain: blocChain.block });
      })
      .catch((err) => {
        console.log("Error fetch api :", err);
      });
  }
  render() {
    return (
      <div className="row">
        <table className="table">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Hash</th>
              <th scope="col">Previous Hash</th>
              <th scope="col">Timestamp</th>
              <th scope="col">Data</th>
              <th scope="col">Nonce</th>
            </tr>
          </thead>
          <tbody>
            {this.state.blocChain.map((block) => {
              return (
                <tr key={block.index}>
                  <th scope="row">{block.index}</th>
                  <td>{block.hash}</td>
                  <td>{block.previous_hash}</td>
                  <td>{block.timestamp}</td>
                  <td>{block.data}</td>
                  <td>{block.nonce}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    );
  }
}

export default Home;
