import { useState, useEffect } from "react";
import axios from "axios";

const useNode = () => {
    const [nodes, setNodes] = useState([])

    useEffect(() => {
        async function initialSet() {
            const initGroupByStarData = await getNodes();
            setNodes(initGroupByStarData);
        }

        initialSet().then(r => {});
    }, []);

    const getNodes = async () => {
        const response = await axios.get(`https://gis-1235303617.ca-central-1.elb.amazonaws.com/topology`);
        console.log(response)
        return response.data;
    }

    return {nodes, setNodes, getNodes}
}
export {useNode};