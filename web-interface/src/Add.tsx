import axios from "axios";
import React from "react";

interface IOwnState {
  inputVal: string;
}

class Add extends React.PureComponent<{}, IOwnState> {
  state = {
    inputVal: "",
  };

  handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    this.setState({ inputVal: event.target.value });
  };

  handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    let input = this.state.inputVal;
    input = input.trim().replace(/\s\s+/g, " ");
    if (input) {
      axios.post(`http://127.0.0.1:4000/add`, { input }).then((res) => {
        console.log(res);
        console.log(res.data);
      });
    }
  };

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <div className="form-group">
          <label htmlFor="data">Data</label>
          <input
            type="text"
            className="form-control"
            id="data"
            value={this.state.inputVal}
            onChange={this.handleChange}
          />
        </div>
        <button type="submit" className="btn btn-primary">
          Send
        </button>
      </form>
    );
  }
}

export default Add;
