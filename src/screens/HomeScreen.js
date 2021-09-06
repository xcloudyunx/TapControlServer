import React, {useState, useEffect} from "react";

import colors from "../config/colors";
import constants from "../config/constants";

import MainBar from "../components/MainBar";
import SideBar from "../components/SideBar";

export default function HomeScreen() {
	const [numOfRows, setNumOfRows] = useState(4);
	const [numOfCols, setNumOfCols] = useState(2);
	const [numOfPages, setNumOfPages] = useState(1);
	const [currentPage, setCurrentPage] = useState(1);
	const [iconButtons, setIconButtons] = useState([[],[]]);
	const [buttonClassName, setButtonClassName] = useState(0);
	const [buttonID, setButtonID] = useState();
	
	useEffect(() => {
		const iB = [[],[]];
		for (let k=1; k<=numOfPages; k++) {
			iB[k] = iconButtons[k].slice(0, numOfRows);
			for (let i=0; i<numOfRows; i++) {
				if (!iB[k][i]) {
					iB[k][i] = [];
				} else {
					iB[k][i] = iB[k][i].slice(0, numOfCols);
				}
				for (let j=iB[k][i].length; j<numOfCols; j++) {
					iB[k][i][j] = "../assets/favicon.png";
				}
			};
		}
		iB.push([])
		setIconButtons(iB);
	}, [numOfRows, numOfCols, numOfPages]);
	
	const handleIconButtonClick = (page, id) => {
		setButtonClassName(page);
		setButtonID(id);
	}
	
	const handleGridSettingsClick = (type, val) => {
		const value = Math.max(val, 1);
		switch (type) {
			case "row":
				setNumOfRows(Math.min(constants.rowMax, value));
				break;
			case "col":
				setNumOfCols(Math.min(constants.colMax, value));
				break;
			case "page":
				const x = Math.min(constants.pageMax, value);
				setNumOfPages(x);
				if (currentPage > x) {
					setCurrentPage(x);
				}
				break;
			default:
				break;
		}
	};
	
	const handleExitClick = () => {
		setButtonClassName(0);
	};
	
	const handlePageChange = (pageNum) => {
		let newPageNum = pageNum%numOfPages;
		if (newPageNum === 0) {
			newPageNum = numOfPages;
		}
		setCurrentPage(newPageNum);
	};
	
	return (
		<div style={styles.background}>
			<MainBar
				numOfRows={numOfRows}
				numOfCols={numOfCols}
				numOfPages={numOfPages}
				currentPage={currentPage}
				iconButtons={iconButtons}
				onChangePageButtonClick={(pageNum) => {handlePageChange(pageNum)}}
				onIconButtonClick={(page, id) => {handleIconButtonClick(page, id)}}
			/>
			<SideBar
				className={buttonClassName}
				id={buttonID}
				numOfRows={numOfRows}
				numOfCols={numOfCols}
				numOfPages={numOfPages}
				onGridSettingsClick={(type, val) => {handleGridSettingsClick(type, val)}}
				onExitClick={handleExitClick}
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