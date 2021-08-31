import React, {useState} from 'react';

import colors from "../config/colors";
import constants from "../config/constants";

import Grid from "../components/Grid";
import SideBar from "../components/SideBar";

export default function HomeScreen() {
	const [numOfRows, setNumOfRows] = useState(4);
	const [numOfCols, setNumOfCols] = useState(2);
	const [numOfPages, setNumOfPages] = useState(1);
	
	const handleChange = (event) => {
		let value = parseInt(event.target.value);
		if (isNaN(value)) {
			value = 1;
		} else {
			value = Math.max(1, value);
		}
		switch (event.target.className) {
			case "rows":
				setNumOfRows(Math.min(constants.rowMax, value));
				break;
			case "columns":
				setNumOfCols(Math.min(constants.colMax, value));
				break;
			case "pages":
				setNumOfPages(Math.min(constants.pageMax, value));
				break;
			default:
				break;
		}
	}
	
	return (
		<div style={styles.background}>
			<Grid numOfRows={numOfRows} numOfCols={numOfCols}/>
			<SideBar numOfRows={numOfRows} numOfCols={numOfCols} numOfPages={numOfPages}onChange={handleChange}/>
		</div>
	);
};

const styles = {
	background: {
		flex: 1,
		backgroundColor: colors.black,
		display: "flex",
	},
};