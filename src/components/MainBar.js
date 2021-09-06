import React from "react";

import constants from "../config/constants";

import Grid from "../components/Grid";
import MainBarOverlay from "../components/MainBarOverlay";

export default function MainBar(props) {
	return (
		<div style={styles.container}>
			<Grid
				id={props.currentPage}
				numOfRows={props.numOfRows}
				numOfCols={props.numOfCols}
				iconButtons={props.iconButtons[props.currentPage]}
				onClick={(page, id) => {props.onIconButtonClick(page, id)}}
			/>
			
			<MainBarOverlay
				currentPage={props.currentPage}
				onClick={(pageNum) => {props.onChangePageButtonClick(pageNum)}}
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