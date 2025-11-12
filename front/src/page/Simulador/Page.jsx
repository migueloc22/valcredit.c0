import { Box, Typography } from "@mui/material";
import React from "react";
import useSimulador from "./hooks/useSimulador.jsx";
import { FormCalcular } from "./components";
import { DataGrid } from "@mui/x-data-grid";
import { esES } from "@mui/x-data-grid/locales";

export const Simulador = () => {
  const { onSubmit, rows, columns } = useSimulador();

  return (
    <Box sx={{ p: 2, mt: 3, position: "relative", minHeight: "80vh" }}>
      <Typography variant="h4" gutterBottom>
        Simulador de Crédito
      </Typography>

      <FormCalcular onSubmit={onSubmit} />

      {rows && rows.length > 0 && (
        <Box sx={{ mt: 3, width: "100%", maxWidth: 900 }}>
          <DataGrid
            rows={rows}
            columns={columns}
            pageSize={10}
            rowsPerPageOptions={[5, 10, 25]}
            localeText={esES.components.MuiDataGrid.defaultProps.localeText}
            autoHeight
          />
        </Box>
      )}
    </Box>
  );
};
