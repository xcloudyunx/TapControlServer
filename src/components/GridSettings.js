import React from 'react';

import colors from "../config/colors";
import constants from "../config/constants";

import NumberInput from "./NumberInput";

export default function GridSettings(props) {
	return (
		<div style={styles.container}>
			<NumberInput title="Rows" value={props.numOfRows} onClick={(val) => {props.onClick("row", val)}}/>
			<NumberInput title="Columns" value={props.numOfCols} onClick={(val) => {props.onClick("col", val)}}/>
			<NumberInput title="Pages" value={props.numOfPages} onClick={(val) => {props.onClick("page", val)}}/>
		</div>
	);
}

const styles = {
	container: {
		flex: 1,
		display: "flex",
		flexDirection: "column",
		padding: "5%",
		backgroundColor: colors.secondary,
		borderTop: constants.border,
	},
};