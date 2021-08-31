import React from 'react';

import colors from "../config/colors";

import ButtonNumbers from "./ButtonNumbers";

export default function SideBar(props) {
	return (
		<div style={styles.container}>
			<div style={{flex:5}}/>
			<ButtonNumbers numOfRows={props.numOfRows} numOfCols={props.numOfCols} numOfPages={props.numOfPages} onChange={props.onChange}/>
		</div>
	);
}

const styles = {
	container: {
		flex: 1,
		display: "flex",
		flexDirection: "column",
		backgroundColor: colors.primary,
	},
};