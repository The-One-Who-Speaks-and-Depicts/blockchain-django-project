import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class BlocksService{

    constructor(){}


    getBlocks() {
        const url = `${API_URL}/api/blocks/`;
        return axios.get(url).then(response => response.data);
    }
    getBlocksByURL(link){
        const url = `${API_URL}${link}`;
        return axios.get(url).then(response => response.data);
    }
    getBlock(height) {
        const url = `${API_URL}/api/blocks/${height}`;
        return axios.get(url).then(response => response.data);
    }
}