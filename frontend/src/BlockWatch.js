import  React, { Component } from  'react';
import  BlocksService  from  './BlocksService';

const  blocksService  =  new  BlocksService();

class  BlocksList  extends  Component {

constructor(props) {
    super(props);
    this.state  = {
        blocks: []
    };
}

componentDidMount() {
    var  self  =  this;
    const { match: { params } } =  this.props;
    var height = params.height;
    blocksService.getBlocks().then(function (result) {
        console.log(result);
        self.setState({ blocks:  result.data, nextPageURL:  result.nextlink})
        var  newArr  =  self.state.blocks.filter(function(obj) {
            return  obj.height  ==  height;
        });

        self.setState({blocks:  newArr})
    });
}


render() {

    return (
        <div  className="blocks--list">
            <table  className="table">
            <thead  key="thead">
            <tr>
                <th>Height</th>
                <th>Hash</th>
                <th>Timestamp</th>
                <th>Transactions</th>
                <th>Miner</th>
            </tr>
            </thead>
            <tbody>
            {this.state.blocks.map( c  =>
                <tr  key={c.height}>
                <td>{c.height}</td>
                <td>{c.hash}  </td>
                <td>{c.timestamp}</td>
                <td>{c.transactions}</td>
                <td>{c.miner}</td>               
            </tr>)}
            </tbody>
            </table>
        </div>
        );
  }
}
export  default  BlocksList;