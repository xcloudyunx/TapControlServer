import React from "react";

import IconButton from "./IconButton";

export default function Row(props) {
	return (
		<div style={styles.container}>
			{props.row.map((col, j) => {
				return (
					<IconButton
						key={j}
						id={props.id*props.numOfCols+j}
						source={col}
						size={props.size}
						onClick={(id) => props.onClick(id)}
					/>
				)
			})}
		</div>
	);
}

const styles = {
	container: {
		display: "flex",
		flexDirection: "row",
		justifyContent: "space-evenly",
		alignItems: "center",
	},
};