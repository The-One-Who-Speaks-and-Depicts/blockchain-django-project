import  React, { Component } from  'react';
import  BlocksService  from  './BlocksService';

const  blocksService  =  new  BlocksService();

class  BlocksList  extends  Component {

constructor(props) {
    super(props);
    this.state  = {
        blocks: [],
        nextPageURL:  ''
    };
    this.nextPage  =  this.nextPage.bind(this);
}

componentDidMount() {
    var  self  =  this;
    blocksService.getBlocks().then(function (result) {
        console.log(result);
        self.setState({ blocks:  result.data, nextPageURL:  result.nextlink})
    });
}


nextPage(){
    var  self  =  this;
    console.log(this.state.nextPageURL);
    blocksService.getBlocksByURL(this.state.nextPageURL).then((result) => {
        self.setState({ blocks:  result.data, nextPageURL:  result.nextlink})
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
                <tr  key={c.pk}>
                <td>{c.height}</td>
                <td>{c.hash}  </td>
                <td>{c.timestamp}</td>
                <td>{c.transactions}</td>
                <td>{c.miner}</td>                
            </tr>)}
            </tbody>
            </table>
            <button  className="btn btn-primary"  onClick=  {  this.nextPage  }>Next</button>
        </div>
        );
  }
}
export  default  BlocksList;