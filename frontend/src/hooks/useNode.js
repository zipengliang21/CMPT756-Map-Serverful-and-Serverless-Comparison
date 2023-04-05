import {useEffect, useState} from "react";
import axios from "axios";

const useNode = () => {
    const [nodes, setNodes] = useState([])
    const [links, setLinks] = useState([])

    useEffect(() => {
        async function initialSet() {
            const initNodes = await getNodes();
            const initTopologies = await getLinks();
            setNodes(initNodes);
            setLinks(initTopologies);
        }

        initialSet().then(r => {});
    }, []);

    const getNodes = async () => {
        const response = await axios.get(`http://gis-1235303617.ca-central-1.elb.amazonaws.com/topology`);
        return response.data.geolocations;
    }

    const getLinks = async () => {
        const response = await axios.get(`http://gis-1235303617.ca-central-1.elb.amazonaws.com/topology`);
        // console.log(response)
        return response.data.topology;
    }

    return {nodes, setNodes, links, setLinks, getNodes, getLinks}
}
export {useNode};