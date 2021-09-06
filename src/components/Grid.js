import React from "react";

import Row from "./Row";

export default function Grid(props) {
	const buttonDim = Math.min(
		window.innerHeight/(props.numOfRows+1),
		(window.innerWidth/2)/(props.numOfCols+1)
	);
	
	return (
		<div id={props.id} style={Object.assign([], styles.container, {display: props.display})}>
			{props.iconButtons.map((row, i) => {
				return(
					<Row
						key={i}
						id={i}
						numOfCols={props.numOfCols}
						row={row}
						size={buttonDim}
						onClick={(id) => props.onClick(props.id, id)}
					/>
				)
			})}
		</div>
	);
}

const styles = {
	container: {
		flex: 1,
		display: "flex",
		flexDirection: "column",
		justifyContent: "space-evenly",
	},
};