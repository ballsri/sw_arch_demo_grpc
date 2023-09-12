import React from "react";
import {
  useDataGrid,
  DataGrid,
  GridColumns,
  EditButton,
  List,
  DeleteButton,
} from "@pankod/refine-mui";

export const HousekeeperList = () => {
  const { dataGridProps } = useDataGrid({
    queryOptions: { retry: false },
    hasPagination: false,
  });

  const columns = React.useMemo<GridColumns<any>>(
    () => [
      {
        field: "id",
        headerName: "Housekeeper id",
        type: "string",
        minWidth: 300,
      },

      {
        field: "firstName",
        headerName: "First Name",
        minWidth: 250,
      },
      {
        field: "lastName",
        headerName: "Last Name",
        minWidth: 250,
      },
      {
        field: "phone",
        headerName: "Phone",
        minWidth: 200,
      },
      {
        field: "actions",
        headerName: "Actions",
        renderCell: function render({ row }) {
          return (
            <>
              <EditButton hideText recordItemId={row.id} />
              <DeleteButton hideText recordItemId={row.id} />
            </>
          );
        },
        align: "center",
        headerAlign: "center",
        minWidth: 80,
      },
    ],
    []
  );

  return (
    <List>
      <DataGrid
        {...dataGridProps}
        getRowId={(row) => row.id}
        columns={columns}
        autoHeight
      />
    </List>
  );
};
