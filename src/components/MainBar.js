import React, {useState} from 'react';

import constants from "../config/constants";

import Grid from "../components/Grid";
import MainBarOverlay from "../components/MainBarOverlay";

export default function MainBar(props) {
	const [currentPage, setCurrentPage] = useState(1);
	
	const handleClick = (pageNum) => {
		let newPageNum = pageNum%props.numOfPages;
		if (newPageNum === 0) {
			newPageNum = props.numOfPages;
		}
		setCurrentPage(newPageNum);
		// need to change it so that changing page numbers 
		// won't screw this up
	};
	
	return (
		<div style={styles.container}>
			{[...Array(props.numOfPages)].map((page, i) => {
				return(
					<Grid
						key={i+1}
						id={i+1}
						numOfRows={props.numOfRows}
						numOfCols={props.numOfCols}
						display={i+1===currentPage ? "flex" : "none"}
					/>
				)
			})}
			// why do buttons stop working when adding overlay????
			
			<MainBarOverlay
				currentPage={currentPage}
				onClick={(pageNum) => {handleClick(pageNum)}}
			/>
		</div>
	);
};

const styles = {
	container: {
		position: "relative",
		flex: 1,
		display: "flex",
		borderRight: constants.border,
	},
};