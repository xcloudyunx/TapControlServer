import React from 'react';

import colors from "../config/colors";
import constants from "../config/constants";

import NumberInput from "./NumberInput";

export default function ButtonNumbers(props) {
	return (
		<div style={styles.container}>
			<NumberInput title="Rows" value={props.numOfRows} max={constants.rowMax} onChange={props.onChange}/>
			{/*<NumberInput title="Columns" value={props.numOfCols} max={constants.colMax} onChange={props.onChange}/>
			<NumberInput title="Pages" value={props.numOfPages} max={constants.pageMax} onChange={props.onChange}/>*/}
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
	},
};