import React, {useState} from 'react';

import colors from "../config/colors";
import constants from "../config/constants";

import MainBar from "../components/MainBar";
import SideBar from "../components/SideBar";

export default function HomeScreen() {
	const [numOfRows, setNumOfRows] = useState(4);
	const [numOfCols, setNumOfCols] = useState(2);
	const [numOfPages, setNumOfPages] = useState(1);
	
	const handleClick = (type, val) => {
		const value = Math.max(val, 1);
		switch (type) {
			case "row":
				setNumOfRows(Math.min(constants.rowMax, value));
				break;
			case "col":
				setNumOfCols(Math.min(constants.colMax, value));
				break;
			case "page":
				setNumOfPages(Math.min(constants.pageMax, value));
				break;
			default:
				break;
		}
	}
	
	return (
		<div style={styles.background}>
			<MainBar
				numOfRows={numOfRows}
				numOfCols={numOfCols}
				numOfPages={numOfPages}
			/>
			<SideBar
				numOfRows={numOfRows}
				numOfCols={numOfCols}
				numOfPages={numOfPages}
				onClick={(type, val) => {handleClick(type, val)}}
			/>
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